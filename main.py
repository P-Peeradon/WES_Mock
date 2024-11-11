from WES_Mock.student import Student
from WES_Mock.unit import Unit
from WES_Mock.enrolment import Enrolment
import re


if __name__ == "__main__":
    print(re.match(r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", "0000-0002-6756-6119"))