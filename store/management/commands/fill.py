from django.core.management import BaseCommand
from store.models import Student

class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Petr', 'second_name': 'Petrov'},
            {'first_name': 'Иван', 'second_name': 'Иванов'},
            {'first_name': 'Семен', 'second_name': 'Семенов'},
            {'first_name': 'Катя', 'second_name': 'Катина'},
            {'first_name': 'Николай', 'second_name': 'Петров'},
            {'first_name': 'Николай', 'second_name': 'Пеков'},
            {'first_name': 'инна', 'second_name': 'Кошкина'}
        ]

        #for student_item in student_list:
        #    Student.objects.create(**student_item)

        # если много добавление , лучше использовать данную контрукцию
        # но данные будут в оперативной памяти и не добавяться в бд
        student_for_create = []
        for student_item in student_list:
            student_for_create.append(
                Student(**student_item)
            )

        # данной командай заносим данные в БД
        Student.objects.bulk_create(student_for_create)