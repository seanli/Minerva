# Site Core

ROLE = (
    ('S', 'Student'),
    ('I', 'Instructor'),
    ('T', 'Tutor'),
)

DEGREE = (
    ('UG', 'Undergraduate'),
    ('BA', 'Bachelor'),
    ('MA', 'Master'),
    ('DC', 'Doctor'),
)

CATEGORY = (
    ('C', 'College'),
    ('U', 'University'),
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
