# Created by andrey.sokolovskiy at 22/01/2023
@new_user_creation
Feature: New user creation in the PIM tab
  As a user I should be able to create a new user

  @tc1b
  Scenario: New user creation
    When I open "PIM" tab
     And I add new employee
         | INFO          | VALUE        |
         | First Name    | Petr         |
         | Last Name     | Ivanoff      |
    Then New Employee Personal Details page is displayed
         | INFO          | VALUE        |
         | Full Name     | Petr Ivanoff |
    When I open "PIM" tab
     And I search for employee
         | INFO          | VALUE        |
         | Employee Name | Petr Ivanoff |
    Then Employee record is found
         | COLUMN                |  VALUE  |
         | First (& Middle) Name | Petr    |
         | Last Name             | Ivanoff |
