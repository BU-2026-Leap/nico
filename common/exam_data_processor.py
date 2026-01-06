from common.contracts import DataProcessor, ExamScore

class ExamDataProcessor(DataProcessor):
    def compute_number_of_unique_students(self, scores: [ExamScore]) -> int:
        """
        Given a list of ExamScore's, computes the number of unique students in the data set
        """
        student_ids = []
        for score in scores:
            if score.student_id not in student_ids:
                student_ids.append(score.student_id)

        unique_students = len(student_ids)
        return unique_students


    def compute_average_final(self, scores: [ExamScore]) -> float:
        """
        Given a list of ExamScore's, computes the average of all final scores
        """
        test_num = 0
        total_scores = 0
        for score in scores:
            if score.exam_name == "final":
                total_scores += float(score.score)
                test_num += 1
        if test_num == 0:
            average_final = 0
        else:
            average_final = float(total_scores/test_num)
        return average_final