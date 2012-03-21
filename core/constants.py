# Site Core

ROLE = (
    ('S', 'Student'),
    ('I', 'Instructor'),
)

DEGREE = (
    ('UG', 'Undergraduate'),
    ('BA', 'Bachelor'),
    ('MA', 'Master'),
    ('DC', 'Doctor'),
)

INSTITUTE_CATEGORY = (
    ('C', 'College'),
    ('U', 'University'),
)

MONTH = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)

YEAR = (
    (-1, 'Previous'),
    (0, 'Current'),
    (1, 'Next'),
)

DURATION = (
    ('T', 'Academic Term'),
    ('D', 'Drop In'),
    ('N', 'Never Ending')
)

# Backstage

TICKET_PRIORITY = (
    (0, 'Blocker'),
    (1, 'Critical'),
    (2, 'Major'),
    (3, 'Normal'),
    (4, 'Minor'),
    (5, 'Trivial'),
)

TICKET_CATEGORY = (
    ('B', 'Bug'),
    ('E', 'Enhancement'),
    ('F', 'Feature'),
    ('T', 'Task'),
    ('C', 'Cosmetic'),
)

TICKET_STATUS = (
    ('L', 'Client'),
    ('N', 'New'),
    ('A', 'Assigned'),
    ('C', 'Closed'),
    ('R', 'Reopened'),
)
