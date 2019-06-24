"""
Collection of functions to put JSON requests into a tidy pandas dataframe structure
"""
import pandas as pd
import json

def tidylist(formList: dict):
    df = pd.DataFrame(columns=['id','title'])
    for pesq in formList['items']:
        df = df.append({'id': pesq['id'],'title': pesq['title']}
        ,ignore_index=True)
    return df

def tidyquestions(formQuestions: dict):
    df = pd.DataFrame(columns=['id_form'
                                ,'title_form'
                                ,'hidden_form'
                                ,'welcome_screens'
                                ,'thankyou_screens'
                                ,'id_question'
                                ,'title_question'
                                ,'type_question'])
    id_form = formQuestions['id']
    title_form = formQuestions['title']
    if 'hidden' in formQuestions:
        hidden_form = formQuestions['hidden']
    else:
        hidden_form = ''
    if 'welcome_screens' in formQuestions:
        welcome_screens = formQuestions['welcome_screens'][0]['title']
    else:
        welcome_screens = ''
    if 'thankyou_screens' in formQuestions:
        thankyou_screens = formQuestions['thankyou_screens'][0]['title']
    else:
        thankyou_screens = ''
    if 'fields' in formQuestions: 
        quest = formQuestions['fields']
        for i in range(len(quest)):
            q = quest[i]
            id_question = q['id'] 
            title_question = q['title']
            type_question = q['type']
            df = df.append({'id_form': id_form
                            ,'title_form': title_form
                            ,'hidden_form': hidden_form
                            ,'welcome_screens': welcome_screens
                            ,'thankyou_screens': thankyou_screens 
                            ,'id_question': id_question
                            ,'title_question': title_question
                            ,'type_question': type_question}
                            ,ignore_index=True)
    else:
        df = df.append({'id_form': id_form
                        ,'title_form': title_form
                        ,'hidden_form': hidden_form
                        ,'welcome_screens': welcome_screens
                        ,'thankyou_screens': thankyou_screens 
                        ,'id_question': ''
                        ,'title_question': ''
                        ,'type_question': ''}
                        ,ignore_index=True)

    return df


def tidyAnswers(formAnswers: dict):
    #create df to store answers
    df = pd.DataFrame(columns=['landing_id'
                            ,'landed_at'
                            ,'submitted_at'
                            ,'user_agent'
                            ,'hidden'
                            ,'calculated'
                            ,'question_id'
                            ,'question_type'
                            ,'question_answer'])

    landing_id = formAnswers['landing_id']
    landed_at = formAnswers['landed_at']
    submitted_at = formAnswers['submitted_at']
    user_agent = formAnswers['metadata']['user_agent']
    if 'hidden' in formAnswers:
        hidden = formAnswers['hidden']
    else:
        hidden = ''
    if 'calculated'in formAnswers:
        calculated = formAnswers['calculated']
    else:
        calculated = ''

    my_answers = formAnswers['answers']
    for my_answer in my_answers:
        question_id = my_answer['field']['id']
        question_type = my_answer['type']
        if question_type == 'choice':
            question_answer = my_answer[question_type]
            question_answer = question_answer['label']
        elif question_type == 'choices':
            question_answer = my_answer[question_type]
            question_answer = question_answer['labels']
        else:
            question_answer = my_answer[question_type]
        df = df.append({'landing_id': landing_id
                        ,'landed_at': landed_at
                        ,'submitted_at': submitted_at
                        ,'user_agent': user_agent
                        ,'hidden': hidden
                        ,'calculated': calculated
                        ,'question_id': question_id
                        ,'question_type': question_type
                        ,'question_answer': question_answer}
                        ,ignore_index=True)
    
    return df