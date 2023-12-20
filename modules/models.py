from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

TERM_TYPE = [
    ('DEFINITION', 'Definition'),
    ('THEOREM', 'Theorem'),
    ('LEMMA', 'Lemma'),
    ('COROLLARY', 'Corollary'),
    ('ALGORITHM', 'Algorithm'),
]

QUESTION_TYPE = [
    ('TRUE_FALSE', 'True or False'),
    ('MULTIPLE_CHOICE', 'Multiple Choice'),
    ('MULTIPLE_ANSWER', 'Multiple Answer'),
    ('NUMERIC', 'Numeric'),
    ('FORMULA', 'Formula'),
    ('LATEX', 'Latex'),
    ('SHORT_ANSWER', 'Short Answer'),
    ('OPEN_ENDED', 'Open-Ended'),
]


class Term(models.Model):
    name = models.CharField(max_length=100)
    definition = models.TextField()
    depends_on = models.ManyToManyField('self', symmetrical=False, blank=True, through='TermDependency')
    term_type = models.CharField(choices=TERM_TYPE, max_length=10, default='DEFINITION')

    def __str__(self):
        return self.name


class TermDependency(models.Model):
    parent_term = models.ForeignKey(Term, related_name='parent_term', on_delete=models.CASCADE)
    child_term = models.ForeignKey(Term, related_name='child_term', on_delete=models.CASCADE)


class Submodule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Reading(Submodule):
    module = models.ForeignKey('Module', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()


class TestBank(Submodule):
    pass


class Question(models.Model):
    test_bank = models.ForeignKey(TestBank, related_name='test_bank', on_delete=models.CASCADE)
    title = models.TextField()
    difficulty = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    question_type = models.CharField(choices=QUESTION_TYPE, max_length=15)
    answer1 = models.TextField(null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    answer4 = models.TextField(null=True, blank=True)
    answer5 = models.TextField(null=True, blank=True)


class Module(models.Model):
    name = models.CharField(max_length=100)
    depends_on = models.ManyToManyField('self', symmetrical=False, blank=True, through='ModuleDependency')
    terms = models.ManyToManyField(Term, blank=True)

    def __str__(self):
        return self.name


class ModuleDependency(models.Model):
    parent_module = models.ForeignKey(Module, related_name='parent_module', on_delete=models.CASCADE)
    child_module = models.ForeignKey(Module, related_name='child_module', on_delete=models.CASCADE)


class ModuleTerm(models.Model):
    module = models.ForeignKey(Module, related_name='module_with_term', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, related_name='term_with_module', on_delete=models.CASCADE)
