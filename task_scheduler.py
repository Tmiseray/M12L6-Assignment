
def format_task(task, level=0):
    """Helper function to format each task & subtask recursively"""
    indent = '   ' * level
    priority_order = {'High': 0, 'Medium': 1, 'Low': 2}

    if level == 0:
        task_str = f"{indent}> {task['name']} (Priority: {task['priority']})"
    elif level == 1:
        task_str = f"{indent}- {task['name']} (Priority: {task['priority']})"
    elif level == 2:
        task_str = f"{indent}~ {task['name']} (Priority: {task['priority']})"
    else:
        task_str = f"{indent}* {task['name']} (Priority: {task['priority']})"

    if task.get('subtask'):
        task['subtask'].sort(key=lambda t: priority_order[t['priority']])
        for sub in task['subtask']:
            task_str += '\n' + format_task(sub, level + 1)
    
    return task_str

def schedule_tasks(task_hierarchy):
    schedule = []
    priority_order = {'High': 0, 'Medium': 1, 'Low': 2}

    task_hierarchy.sort(key = lambda task: priority_order[task['priority']])

    for task in task_hierarchy:
        schedule.append(format_task(task, 0))
    return '\n'.join(schedule)


task_hierarchy = [
    {'id': 1, 'name': 'Attend meetings', 'subtask': [
        {'id': 11, 'name': 'Team member collaboration meeting', 'subtask': [
            {'id': 111, 'name': 'Process improvement ideas', 'subtask': None, 'priority': 'Medium'},
            {'id': 112, 'name': 'Create project idea outline', 'subtask': None, 'priority': 'Medium'},
            {'id': 113, 'name': 'Schedule next collaboration meeting', 'subtask': None, 'priority': 'High'},
        ], 'priority': 'Medium'},
        {'id': 12, 'name': 'Team meeting', 'subtask': [
            {'id': 121, 'name': 'Take notes', 'subtask': [
                {'id': 1211, 'name': 'Format notes', 'subtask': None, 'priority': 'High'},
            ], 'priority': 'High'},
        ], 'priority': 'High'},
        {'id': 13, 'name': 'Development time for teach-back', 'subtask': [
            {'id': 131, 'name': 'Pick 1 team member pain point', 'subtask': None, 'priority': 'High'},
            {'id': 132, 'name': 'Create outline for powerpoint presentation', 'subtask': [
                {'id': 1321, 'name': 'Collect all manual page references for pain point', 'subtask': None, 'priority': 'Medium'},
                {'id': 1322, 'name': 'Collect screen recordings of any/all video examples', 'subtask': None, 'priority': 'Medium'},
                {'id': 1323, 'name': 'Collect screenshots of any/all example pictures', 'subtask': None, 'priority': 'Medium'},
            ], 'priority': 'Medium'},
            {'id': 133, 'name': 'Implement outline', 'subtask': [
                {'id': 1331, 'name': 'Create any/all tables', 'subtask': None, 'priority': 'Low'},
                {'id': 1332, 'name': 'Insert any/all examples', 'subtask': None, 'priority': 'Low'},
                {'id': 1333, 'name': 'Format powerpoint', 'subtask': None, 'priority': 'Low'},
            ], 'priority': 'Low'},
            {'id': 134, 'name': 'Test run presentation before submission to Supervisor for approval', 'subtask': None, 'priority': 'Low'},
        ], 'priority': 'Low'},
    ], 'priority': 'High'},
    {'id': 2, 'name': 'Reorganize desk', 'subtask': None, 'priority': 'Low'},
    {'id': 3, 'name': 'Timesheet', 'subtask': [
        {'id': 31, 'name': 'Compare pre-entered times to actual login/logout times', 'subtask': [
            {'id': 311, 'name': 'Make adjustments as needed', 'subtask': None, 'priority': 'High'},
            {'id': 312, 'name': 'Ensure Holiday times (if any) are included', 'subtask': None, 'priority': 'High'},
            {'id': 313, 'name': 'Ensure any sick leave days are included', 'subtask': None, 'priority': 'High'},
            {'id': 314, 'name': 'Ensure any days from previous pay period are updated (if needed)', 'subtask': None, 'priority': 'High'},
        ], 'priority': 'High'},
        {'id': 32, 'name': 'Save timesheet after any adjustments', 'subtask': None, 'priority': 'High'},
        {'id': 33, 'name': 'Submit timesheet', 'subtask': None, 'priority': 'High'},
    ], 'priority': 'High'},
    {'id': 4, 'name': 'Send Mindful/Positive GIF/message in team chat', 'subtask': None, 'priority': 'Low'},
]

print(schedule_tasks(task_hierarchy))