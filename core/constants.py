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
    (0, 'Highest'),
    (1, 'High'),
    (2, 'Normal'),
    (3, 'Low'),
    (4, 'Lowest'),
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
