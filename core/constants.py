import logging

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

GRADE = (
    (8, 'SSS'),
    (7, 'SS'),
    (6, 'S'),
    (5, 'A+'),
    (4, 'A'),
    (3, 'B+'),
    (2, 'B'),
    (1, 'C+'),
    (0, 'C'),
    (-1, 'C-'),
    (-2, 'D'),
    (-3, 'D-'),
    (-4, 'F'),
)

GRADE_MAX = 8
GRADE_MIN = -4
GRADE_STEP = 100

SKILL_RATING = (
    (1, 'Novice'),
    (2, 'Familiar'),
    (3, 'Average'),
    (4, 'Expert'),
    (5, 'Guru')
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

LOG_LEVEL = (
    (logging.FATAL, 'Fatal'),
    (logging.CRITICAL, 'Critical'),
    (logging.ERROR, 'Error'),
    (logging.WARNING, 'Warning'),
    (logging.INFO, 'Info'),
    (logging.DEBUG, 'Debug'),
)
