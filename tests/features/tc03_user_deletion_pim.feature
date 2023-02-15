# Created by andrey.sokolovskiy at 22/01/2023
@user_deletion
Feature: User Deletion
  As a user I want to delete user record

  @tc3b
  Scenario: User deletion by clicking trash button PIM
    When I open "PIM" tab
     And I search for employee by entering "3" symbols of his name and selecting him in auto-suggest list
         | INFO          | VALUE        |
         | Employee Name | Petr Ivanoff |
    Then Employee record is found
         | COLUMN                |  VALUE       |
         | First (& Middle) Name | Petr         |
         | Last Name             | Ivanoff      |
         | Job Title             | QA Engineer  |
    When I delete the founded employee
     And I open "PIM" tab
     And I search for employee
         | INFO          | VALUE        |
         | Employee Name | Petr Ivanoff |
    Then Employee record is NOT found



