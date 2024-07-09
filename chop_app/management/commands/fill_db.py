from random import choices
from django.core.management.base import BaseCommand
from ...models import Course, Student, Enrollment


class Command(BaseCommand):
    help = "Generate fake authors and posts."


    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Student ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            student = Student(name=f'name_{i}')
            student.save()
        for g in range(1, count + 1):
            course = Course(name=f'name_{g}')
            course.save()
        for j in range(1, count + 1):
            env = Enrollment(
            student= student,
            course = course
            )
            env.save()