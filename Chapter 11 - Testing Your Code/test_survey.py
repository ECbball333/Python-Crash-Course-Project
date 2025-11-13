import pytest
from survey import AnonymousSurvey

@pytest.fixture

def language_survey():
    """A survey that will be available to all test functions"""
    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    #question = 'What language did you first learn to speak?'
    #language_survey = AnonymousSurvey(question)
    language_survey.store_responses('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three responses are stored properly"""
    #question = 'What language did you learn to speak?'
    #language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_responses(response)

    for response in responses:
        assert response in language_survey.responses