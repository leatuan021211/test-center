from rest_framework import serializers
from .models import Assignment, AssignmentQuestion, AssignmentMultiAnswer, AssignmentEssayAnswer, AssignmentFillBlankAnswer

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        

class AssignmentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentQuestion
        fields = ['question__text', 'question__question_type']
        

class AssignmentMultiAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentMultiAnswer
        fields = ['question', 'answer', 'is_correct']


class AssignmentEssayAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentEssayAnswer
        fields = ['question', 'answer']


class AssignmentFillBlankAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentFillBlankAnswer
        fields = ['question', 'position', 'answer']


class AssignmentSubmissionSerializer(serializers.Serializer):
    multi_answers = AssignmentMultiAnswerSerializer(many=True, required=False)
    essay_answers = AssignmentEssayAnswerSerializer(many=True, required=False)
    fill_blank_answers = AssignmentFillBlankAnswerSerializer(many=True, required=False)

    def create(self, validated_data):
        # Handle each answer type and save them to the database
        multi_answers_data = validated_data.pop('multi_answers', [])
        essay_answers_data = validated_data.pop('essay_answers', [])
        fill_blank_answers_data = validated_data.pop('fill_blank_answers', [])

        # Create AssignmentMultiAnswer records
        for answer_data in multi_answers_data:
            AssignmentMultiAnswer.objects.create(**answer_data)

        # Create AssignmentEssayAnswer records
        for answer_data in essay_answers_data:
            AssignmentEssayAnswer.objects.create(**answer_data)

        # Create AssignmentFillBlankAnswer records
        for answer_data in fill_blank_answers_data:
            AssignmentFillBlankAnswer.objects.create(**answer_data)

        return validated_data
