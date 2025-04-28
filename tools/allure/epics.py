from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS System"
    STUDENT = "Student system"
    ADMINISTRATOR = "Administrator system"
