# Edit Task Feature Specification

## Title
Edit Task

## User Story
As a user, I want to edit an existing task so that I can keep task information accurate and up to date.

## Feature Description
Allows users to modify the title and description of an existing task.

## Functional Requirements
- User can select an existing task.
- User can update task title and description.
- System saves changes and refreshes the task list.

## GIVEN-WHEN-THEN Scenario
**GIVEN** an existing task is displayed  
**WHEN** the user updates the task title and saves changes  
**THEN** the updated task information is displayed in the task list.

## Non-Functional Requirement (NFR)
- Task update response time shall be ≤ 1 second for 95% of requests.

## Edge Case
- If the task being edited was deleted by another user before save, the system shall show an error and prevent the update.

## Acceptance Criteria
- Existing task can be updated successfully.
- Updated values are persisted.
- Appropriate error shown if task no longer exists.

## Definition of Done
- Feature implemented.
- Unit tests pass.
- Acceptance criteria verified.
- Documentation updated.
