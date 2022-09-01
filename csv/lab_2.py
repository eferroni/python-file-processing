import csv

class Exam:
    def __init__(self) -> None:
        self.exam = {}

    def append_result(self, row):
        name = row['Exam Name']
        candidate_id = row['Candidate ID']
        score = row['Score']
        grade = row['Grade']

        if self.exam.get(name) is None:
            self.exam[name] = {
                'candidates': 1,
                'candidates_ids': [candidate_id],
                'passed': 1 if grade == 'Pass' else 0,
                'failed': 1 if grade == 'Fail' else 0,
                'best': score,
                'worst': score
            }
        else:
            if candidate_id not in self.exam[name]['candidates_ids']:
                self.exam[name]['candidates'] += 1
                self.exam[name]['candidates_ids'].append(candidate_id)

            if grade == 'Pass':
                self.exam[name]['passed'] += 1
            else:
                self.exam[name]['failed'] += 1

            if score > self.exam[name]['best']:
                self.exam[name]['best'] = score
            
            if score < self.exam[name]['worst']:
                self.exam[name]['worst'] = score


exam = Exam()
with open('exam_results.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        exam.append_result(row)

with open('report.csv', 'w', newline='') as csvfile:
    fieldnames = ['Exam Name','Number of Candidates','Number of Passed Exams','Number of Failed Exams','Best Score','Worst Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
    writer.writeheader()
    for key in exam.exam:
        writer.writerow({
            'Exam Name': key,
            'Number of Candidates': exam.exam[key]['candidates'],
            'Number of Passed Exams': exam.exam[key]['passed'],
            'Number of Failed Exams': exam.exam[key]['failed'],
            'Best Score': exam.exam[key]['best'],
            'Worst Score': exam.exam[key]['worst']
        })
    