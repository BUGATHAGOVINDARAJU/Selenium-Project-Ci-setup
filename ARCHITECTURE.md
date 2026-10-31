# Architecture Documentation

## Overview

This project implements an automated job search agent using Selenium WebDriver with a Behave BDD framework. The architecture follows SOLID principles and industry-standard design patterns.

## Design Patterns

### 1. Page Object Model (POM)
**Location**: `pages/` directory

**Purpose**: Separates page structure from test logic, improving maintainability and reusability.

**Implementation**:
- `BasePage`: Abstract base class with common web interactions
- `IndeedSearchPage`: Encapsulates search page elements and actions
- `IndeedResultsPage`: Handles results extraction and pagination

**Benefits**:
- Single source of truth for page elements
- Easy to update when UI changes
- Reusable across different test scenarios

### 2. Factory Pattern
**Location**: `utils/webdriver_factory.py`

**Purpose**: Centralized WebDriver creation with browser abstraction.

**Implementation**:
```python
driver = WebDriverFactory.get_driver()  # Returns configured driver
```

**Benefits**:
- Supports multiple browsers (Chrome, Firefox, Edge)
- Consistent driver configuration
- Easy to switch browsers via environment variables

### 3. Singleton Pattern
**Location**: `utils/logger.py`

**Purpose**: Single logger instance per module to avoid duplicate logs.

**Implementation**:
```python
logger = Logger.get_logger(__name__)
```

**Benefits**:
- Consistent logging format
- Prevents duplicate log entries
- Centralized log configuration

### 4. Strategy Pattern
**Location**: `utils/data_handler.py`

**Purpose**: Multiple data export strategies (JSON, CSV, Excel).

**Implementation**:
```python
DataHandler.save_jobs(data, format_type='json')  # or 'csv', 'excel'
```

**Benefits**:
- Easy to add new export formats
- Runtime format selection
- Consistent interface

## Architecture Layers

### 1. Configuration Layer
**Directory**: `config/`

**Responsibilities**:
- Environment variable management
- Application settings
- Directory creation

**Key Files**:
- `config.py`: Central configuration class

### 2. Utility Layer
**Directory**: `utils/`

**Responsibilities**:
- WebDriver management
- Logging
- Data handling
- Common utilities

**Key Files**:
- `webdriver_factory.py`: Browser initialization
- `logger.py`: Logging configuration
- `data_handler.py`: Data export/import

### 3. Page Layer
**Directory**: `pages/`

**Responsibilities**:
- Page element definitions
- Page-specific actions
- Element interaction logic

**Key Files**:
- `base_page.py`: Common page operations
- `indeed_search_page.py`: Search functionality
- `indeed_results_page.py`: Results extraction

### 4. Test Layer
**Directory**: `features/`

**Responsibilities**:
- BDD test scenarios
- Step definitions
- Test hooks

**Key Files**:
- `job_search.feature`: Gherkin scenarios
- `steps/job_search_steps.py`: Step implementations
- `environment.py`: Behave hooks

### 5. Application Layer
**Directory**: Root

**Responsibilities**:
- Standalone execution
- CLI interface
- Orchestration

**Key Files**:
- `job_search_agent.py`: Main application class

## Data Flow

```
User Input
    ↓
JobSearchAgent.run()
    ↓
WebDriverFactory.get_driver()
    ↓
IndeedSearchPage.search_jobs()
    ↓
IndeedResultsPage.extract_jobs_from_multiple_pages()
    ↓
DataHandler.save_jobs()
    ↓
Output File (JSON/CSV/Excel)
```

## Component Interaction

```
┌─────────────────────────────────────────────────┐
│           Job Search Agent (Main)               │
└───────────────┬─────────────────────────────────┘
                │
    ┌───────────┴───────────┐
    │                       │
    ▼                       ▼
┌─────────┐           ┌──────────┐
│ Config  │           │  Utils   │
└─────────┘           └──────────┘
                            │
                ┌───────────┼───────────┐
                │           │           │
                ▼           ▼           ▼
          ┌─────────┐ ┌────────┐ ┌──────────┐
          │ Logger  │ │WebDriver│ │  Data    │
          │         │ │ Factory │ │ Handler  │
          └─────────┘ └────────┘ └──────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │  Page Objects│
                    └──────────────┘
                            │
                ┌───────────┼───────────┐
                │           │           │
                ▼           ▼           ▼
          ┌─────────┐ ┌──────────┐ ┌──────────┐
          │  Base   │ │  Search  │ │ Results  │
          │  Page   │ │   Page   │ │   Page   │
          └─────────┘ └──────────┘ └──────────┘
```

## Error Handling Strategy

### 1. Graceful Degradation
- Multiple element locator strategies
- Fallback mechanisms for missing elements
- Continue execution when non-critical elements fail

### 2. Logging
- All errors logged with context
- Different log levels (DEBUG, INFO, ERROR)
- Separate file and console logging

### 3. Exception Propagation
- Critical errors propagate to caller
- Non-critical errors logged and handled
- Clean resource cleanup in finally blocks

## Scalability Considerations

### Current Implementation
- Single-threaded execution
- Sequential page processing
- Local file storage

### Future Enhancements
- Parallel browser instances
- Distributed execution
- Database storage
- API endpoints
- Containerization (Docker)

## Testing Strategy

### BDD Tests (Behave)
- Feature files in Gherkin syntax
- Step definitions in Python
- Scenario-based testing

### Test Levels
1. **Milestone 1 Tests**: Navigation and search
2. **Milestone 2 Tests**: Data extraction and pagination

### Test Execution
```bash
behave                    # All tests
behave --tags=milestone1  # Specific milestone
behave --tags=milestone2  # Specific milestone
```

## Configuration Management

### Environment Variables
- Stored in `.env` file
- Loaded via `python-dotenv`
- Type-safe access via Config class

### Configuration Hierarchy
1. Environment variables (.env)
2. Default values (config.py)
3. Runtime overrides (command-line args)

## Logging Architecture

### Log Levels
- **DEBUG**: Detailed diagnostic information (file only)
- **INFO**: General informational messages (file + console)
- **ERROR**: Error events (file + console)

### Log Format
```
YYYY-MM-DD HH:MM:SS - module_name - LEVEL - message
```

### Log Rotation
- Daily log files
- Named by module and date
- Stored in `logs/` directory

## Security Considerations

### Current Implementation
- No sensitive data in code
- Environment variables for configuration
- .gitignore for sensitive files

### Recommendations for Production
- API key encryption
- Proxy rotation
- Rate limiting
- CAPTCHA handling
- User-agent rotation

## Performance Optimization

### Current Optimizations
- Implicit and explicit waits
- Smart element location
- Efficient data structures
- Minimal DOM queries

### Future Optimizations
- Parallel execution
- Caching mechanisms
- Database indexing
- API response caching

## Maintainability Features

1. **Modular Design**: Each component has single responsibility
2. **Clear Naming**: Descriptive names for classes and methods
3. **Documentation**: Inline comments and README files
4. **Type Hints**: Python type annotations (can be added)
5. **Consistent Style**: PEP 8 compliance

## Extensibility Points

1. **New Job Boards**: Add new page objects
2. **New Browsers**: Extend WebDriverFactory
3. **New Export Formats**: Add methods to DataHandler
4. **New Test Scenarios**: Add feature files
5. **Custom Filters**: Extend results page logic

## Dependencies

### Core Dependencies
- `selenium`: Web automation
- `behave`: BDD framework
- `webdriver-manager`: Driver management
- `python-dotenv`: Environment variables

### Data Dependencies
- `pandas`: Data manipulation
- `openpyxl`: Excel support

### Testing Dependencies
- `pytest`: Unit testing framework
- `allure-behave`: Test reporting

## Deployment Considerations

### Local Development
- Virtual environment
- Manual execution
- Local file storage

### Production Deployment
- Docker container
- Scheduled execution (cron/Task Scheduler)
- Cloud storage integration
- Monitoring and alerting

## Code Quality

### Standards
- PEP 8 style guide
- Meaningful variable names
- DRY principle
- SOLID principles

### Best Practices
- Error handling
- Resource cleanup
- Logging
- Configuration management
- Documentation
