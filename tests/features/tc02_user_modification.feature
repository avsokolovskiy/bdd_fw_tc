# Created by andrey.sokolovskiy at 22/01/2023
@user_modification
Feature: user_modification
  As a user I want to modify any user profile details

  @tc2b
  Scenario: Add missing user information in Job Details
    When I open "PIM" tab
     And I search for employee
         | INFO          | VALUE        |
         | Employee Name | Petr Ivanoff |
    Then Employee record is found
         | COLUMN                |  VALUE  |
         | First (& Middle) Name | Petr    |
         | Last Name             | Ivanoff |
         | Job Title             |         |
    When I update job title to 'QA Engineer'
     And I open "PIM" tab
     And I search for employee
         | INFO          | VALUE        |
         | Employee Name | Petr Ivanoff |
    Then Employee record is found
         | COLUMN                |  VALUE       |
         | First (& Middle) Name | Petr         |
         | Last Name             | Ivanoff      |
         | Job Title             | QA Engineer  |
