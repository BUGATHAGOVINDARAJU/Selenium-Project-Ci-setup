from job_search_agent import JobSearchAgent
from utils.logger import Logger

logger = Logger.get_logger(__name__)

def example_basic_search():
    print("\n" + "="*60)
    print("Example 1: Basic Job Search")
    print("="*60)
    
    agent = JobSearchAgent()
    
    jobs_data, file_path = agent.run(
        job_title="Python Developer",
        location="San Francisco",
        max_pages=2,
        output_format="json"
    )
    
    print(f"\nFound {len(jobs_data)} jobs")
    print(f"Results saved to: {file_path}")
    
    if jobs_data:
        print("\nFirst 3 jobs:")
        for i, job in enumerate(jobs_data[:3], 1):
            print(f"\n{i}. {job['title']}")
            print(f"   Company: {job['company']}")
            print(f"   Location: {job['location']}")
            print(f"   Salary: {job['salary'] or 'Not specified'}")

def example_multiple_searches():
    print("\n" + "="*60)
    print("Example 2: Multiple Searches with Different Formats")
    print("="*60)
    
    searches = [
        ("Data Analyst", "Boston", 2, "json"),
        ("QA Engineer", "Seattle", 2, "csv"),
        ("DevOps Engineer", "Austin", 2, "excel"),
    ]
    
    for job_title, location, pages, format_type in searches:
        print(f"\nSearching for {job_title} in {location}...")
        
        agent = JobSearchAgent()
        jobs_data, file_path = agent.run(job_title, location, pages, format_type)
        
        print(f"  ✓ Found {len(jobs_data)} jobs")
        print(f"  ✓ Saved as {format_type}: {file_path}")

def example_with_error_handling():
    print("\n" + "="*60)
    print("Example 3: Search with Error Handling")
    print("="*60)
    
    agent = JobSearchAgent()
    
    try:
        jobs_data, file_path = agent.run(
            job_title="Software Engineer",
            location="New York",
            max_pages=3,
            output_format="json"
        )
        
        if jobs_data:
            print(f"\n✓ Successfully extracted {len(jobs_data)} jobs")
            
            unique_companies = set(job['company'] for job in jobs_data if job['company'])
            print(f"✓ Found jobs from {len(unique_companies)} different companies")
            
            jobs_with_salary = [job for job in jobs_data if job['salary']]
            print(f"✓ {len(jobs_with_salary)} jobs have salary information")
            
        else:
            print("\n⚠ No jobs found matching the criteria")
            
    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}")
        logger.error(f"Search failed: {str(e)}")

def main():
    print("\n" + "="*60)
    print("Automated Job Search Agent - Example Usage")
    print("="*60)
    
    try:
        example_basic_search()
        
        print("\n" + "="*60)
        input("Press Enter to continue to next example...")
        
        example_multiple_searches()
        
        print("\n" + "="*60)
        input("Press Enter to continue to next example...")
        
        example_with_error_handling()
        
    except KeyboardInterrupt:
        print("\n\nExecution interrupted by user")
    except Exception as e:
        print(f"\n\nError: {str(e)}")
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("Check the 'output' folder for generated files")
    print("Check the 'logs' folder for execution logs")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
