import azure.cognitiveservices.speech as speechsdk
import time
import keys

reference_text = open('Welcome.txt', 'r').read()
input_audio = 'ezzat.wav'

def recognize_from_file(reference_text, input_audio):

    speech_config = speechsdk.SpeechConfig(subscription=keys.azure, region="westus")
    audio_config = speechsdk.audio.AudioConfig(filename=input_audio)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(
        reference_text=reference_text,
        grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
        granularity=speechsdk.PronunciationAssessmentGranularity.Phoneme,
        enable_miscue=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config)
    pronunciation_assessment_config.apply_to(speech_recognizer)

    done = False

    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        nonlocal done        
        done = True

    def grade(result):
        pronunciation_result = speechsdk.PronunciationAssessmentResult(result)
        print('    Accuracy score: {}, Pronunciation score: {}, Completeness score : {}, FluencyScore: {}'.format(
            pronunciation_result.accuracy_score, pronunciation_result.pronunciation_score,
            pronunciation_result.completeness_score, pronunciation_result.fluency_score
        ))
        print('  Word-level details:')
        for idx, word in enumerate(pronunciation_result.words):
            print('    {}: word: {}, accuracy score: {}, error type: {};'.format(
                idx + 1, word.word, word.accuracy_score, word.error_type
            ))

    #speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt.result)))
    speech_recognizer.recognized.connect(lambda evt: grade(evt.result))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(.5)
    speech_recognizer.stop_continuous_recognition_async()

recognize_from_file(reference_text, input_audio)
