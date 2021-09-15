from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Choice(models.Model):
    question = models.ForeignKey(
        "Question", related_name="choices", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=64, default="Введите значение")


class Question(models.Model):
    class Type:
        TEXT = "TEXT"
        CHOICE = "CHOICE"
        MULTICHOICE = "MULTICHOICE"

        choices = (
            (TEXT, "TEXT"),
            (CHOICE, "CHOICE"),
            (MULTICHOICE, "MULTICHOICE"),
        )

    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)
    type = models.CharField(
        "Тип вопроса", max_length=11, choices=Type.choices, default=Type.TEXT
    )
    text = models.CharField("Текст вопроса", max_length=256)

    def __str__(self):
        return self.text


class Poll(models.Model):
    title = models.CharField("Название", max_length=256)
    start_date = models.DateField(
        "Дата публикации", auto_now_add=True, editable=False
    )
    end_date = models.DateField("Дата окончания")
    description = models.TextField("Описание", max_length=1024)

    def __str__(self):
        return self.title


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    date = models.DateTimeField("Дата публикации", auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.ForeignKey(
        Vote, related_name="answers", on_delete=models.CASCADE
    )
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    value = models.CharField(max_length=128, blank=True, null=True)
