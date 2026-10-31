Feature: Automated Job Search on Indeed
  As a job seeker
  I want to automate job search on Indeed
  So that I can efficiently find relevant job opportunities

  Background:
    Given I am on the Indeed job board website

  @milestone1
  Scenario: Search for jobs with specific criteria
    When I enter "Software Engineer" as job title
    And I enter "Benguluru" as location
    And I click the search button
    Then I should see job search results

  @milestone1
  Scenario Outline: Search for different job positions
    When I enter "<job_title>" as job title
    And I enter "<location>" as location
    And I click the search button
    Then I should see job search results

    Examples:
      | job_title        | location      |
      | Python Developer | Hyderabad |
      | QA Engineer      | Benguluru       |
      | DevOps Engineer  | Chennai        |

  @milestone2 @test123
  Scenario: Extract job details from search results
    When I search for "Data Analyst" jobs in "Benguluru"
    Then I should be able to extract job listings with following details:
      | field_name |  
      | title       |
      | company     |
      | location    |
      | description |

  @milestone2
  Scenario: Extract jobs from multiple pages
    When I search for "Java Developer" jobs in "Benguluru"
    And I extract jobs from 1 pages
    Then I should have extracted multiple job listings
    And the job listings should be saved in "json" format

  @milestone2
  Scenario: Handle pagination and extract all jobs
    When I search for "Frontend Developer" jobs in "Benguluru"
    And I navigate through all available pages up to 1 pages
    Then all job listings should be extracted
    And the data should be saved to output directory

  @milestone2
  Scenario: Save job listings to database
    When I search for "Backend Developer" jobs in "Benguluru"
    And I extract jobs from 1 pages
    Then I should have extracted multiple job listings
    And the job listings should be saved in "database" format
