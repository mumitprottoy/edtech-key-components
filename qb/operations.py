from .models import (
    AdmissionTest,
    University,
    QuestionMetaData,
    Appearance,
    Question,
    Passage
)

def get_passage(metadata: QuestionMetaData):
    return None if (
        not metadata.has_passage) else (
            Passage.objects.get(metadata=metadata))

def get_options(question: Question) -> list:
    return list(question.options.all())

def get_renderable_package(metadata: QuestionMetaData, for_report=False) -> dict:
    passage = get_passage(metadata)
    for question in metadata.questions.all():
        pass

def get_all_universities_under_admission_test_list(admission_tests: list) -> list:
    universities = list()
    for adm_test in admission_tests:
        universities += list(adm_test.universities.all())
    return universities

def get_all_metadata_id_under_university_list(universities: list) -> list:
    return list(set([appr.metadata.id for appr in Appearance.objects.filter(
        university__in=universities
    )]))
