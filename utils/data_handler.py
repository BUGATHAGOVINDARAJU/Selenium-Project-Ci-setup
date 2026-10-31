import json
import csv
import pandas as pd
import sqlite3
from datetime import datetime
from pathlib import Path
from config.config import Config
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class DataHandler:
    
    @staticmethod
    def save_jobs(jobs_data, format_type=None, filename=None):
        Config.create_directories()
        
        format_type = format_type or Config.OUTPUT_FORMAT
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if filename is None:
            filename = f"job_listings_{timestamp}"
        
        output_path = Path(Config.OUTPUT_PATH)
        
        if format_type == 'json':
            file_path = output_path / f"{filename}.json"
            DataHandler._save_json(jobs_data, file_path)
        elif format_type == 'csv':
            file_path = output_path / f"{filename}.csv"
            DataHandler._save_csv(jobs_data, file_path)
        elif format_type == 'excel':
            file_path = output_path / f"{filename}.xlsx"
            DataHandler._save_excel(jobs_data, file_path)
        elif format_type == 'database' or format_type == 'db':
            file_path = output_path / f"{filename}.db"
            DataHandler._save_to_database(jobs_data, file_path)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
        
        logger.info(f"Saved {len(jobs_data)} jobs to {file_path}")
        return str(file_path)
    
    @staticmethod
    def _save_json(data, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    @staticmethod
    def _save_csv(data, file_path):
        if not data:
            logger.warning("No data to save")
            return
        
        keys = data[0].keys()
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    @staticmethod
    def _save_excel(data, file_path):
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False, engine='openpyxl')
    
    @staticmethod
    def _save_to_database(data, db_path):
        if not data:
            logger.warning("No data to save to database")
            return
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS job_listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                salary TEXT,
                url TEXT,
                extracted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        for job in data:
            cursor.execute('''
                INSERT INTO job_listings (title, company, location, description, salary, url)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                job.get('title', ''),
                job.get('company', ''),
                job.get('location', ''),
                job.get('description', ''),
                job.get('salary', ''),
                job.get('url', '')
            ))
        
        conn.commit()
        conn.close()
        logger.info(f"Saved {len(data)} jobs to database: {db_path}")
    
    @staticmethod
    def load_jobs(file_path):
        file_path = Path(file_path)
        
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return []
        
        if file_path.suffix == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif file_path.suffix == '.csv':
            df = pd.read_csv(file_path)
            return df.to_dict('records')
        elif file_path.suffix == '.xlsx':
            df = pd.read_excel(file_path)
            return df.to_dict('records')
        elif file_path.suffix == '.db':
            return DataHandler._load_from_database(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")
    
    @staticmethod
    def _load_from_database(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT title, company, location, description, salary, url FROM job_listings')
        rows = cursor.fetchall()
        
        jobs = []
        for row in rows:
            jobs.append({
                'title': row[0],
                'company': row[1],
                'location': row[2],
                'description': row[3],
                'salary': row[4],
                'url': row[5]
            })
        
        conn.close()
        return jobs
