from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exam, Question, Choice, Submission

def exam_list(request):
    exams = Exam.objects.all().order_by('-created_at')
    return render(request, 'exams/exam_list.html', {'exams': exams})

@login_required(login_url='login')
def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all()

    participant_name = request.user.get_full_name() or request.user.username

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                try:
                    choice = Choice.objects.get(id=selected_choice_id)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        submission = Submission.objects.create(
            participant_name=participant_name,
            exam=exam,
            score=score,
            total_questions=total_questions
        )
        return redirect('exam_result', submission_id=submission.id)

    return render(request, 'exams/take_exam.html', {'exam': exam, 'questions': questions, 'full_name': participant_name})

def exam_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'exams/result.html', {'submission': submission})
