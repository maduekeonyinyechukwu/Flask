-- View all tasks (Read)
SELECT * FROM task;

-- Create a new task
INSERT INTO task (title, description, status)
VALUES ('Buy groceries', 'Milk, Eggs, Bread', 'Pending');

-- Update task with id = 3 from 'Pending' to 'Completed'
UPDATE task
SET status = 'Completed'
WHERE id = 3;

-- Delete task with id = 2
DELETE FROM task
WHERE id = 2;
