
function formatTask(task, level=0) {
    // Helper function to format each task & subtask recursively
    const indent = '   '.repeat(level);
    const priorityOrder = {'High': 0, 'Medium': 1, 'Low': 2};
    let taskString;

    if (level === 0) {
        taskString = `${indent}> ${task.name} (Priority: ${task.priority})`;
    } else if (level === 1) {
        taskString = `${indent}- ${task.name} (Priority: ${task.priority})`;
    } else if (level === 2) {
        taskString = `${indent}~ ${task.name} (Priority: ${task.priority})`;
    } else {
        taskString = `${indent}* ${task.name} (Priortity: ${task.priority})`;
    }

    if (task.subtask) {
        task.subtask.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);

        task.subtask.forEach(sub => {
            taskString += '\n' + formatTask(sub, level + 1);
        });
    }
    return taskString;
}

function scheduleTasks(taskHierarchy) {
    const priorityOrder = {'High': 0, 'Medium': 1, 'Low': 2};
    let schedule = [];

    taskHierarchy.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);
    taskHierarchy.forEach(task => {
        schedule.push(formatTask(task, 0));
    });
    return schedule.join('\n');
}

const taskHierarchy = [
    {id: 1, name: 'Attend meetings', subtask: [
        {id: 11, name: 'Team member collaboration meeting', subtask: [
            {id: 111, name: 'Process improvement ideas', subtask: null, priority: 'Medium'},
            {id: 112, name: 'Create project idea outline', subtask: null, priority: 'Medium'},
            {id: 113, name: 'Schedule next collaboration meeting', subtask: null, priority: 'High'},
        ], priority: 'Medium'},
        {id: 12, name: 'Team meeting', subtask: [
            {id: 121, name: 'Take notes', subtask: [
                {id: 1211, name: 'Format notes', subtask: null, priority: 'High'},
            ], priority: 'High'},
        ], priority: 'High'},
        {id: 13, name: 'Development time for teach-back', subtask: [
            {id: 131, name: 'Pick 1 team member pain point', subtask: null, priority: 'High'},
            {id: 132, name: 'Create outline for powerpoint presentation', subtask: [
                {id: 1321, name: 'Collect all manual page references for pain point', subtask: null, priority: 'Medium'},
                {id: 1322, name: 'Collect screen recordings of any/all video examples', subtask: null, priority: 'Medium'},
                {id: 1323, name: 'Collect screenshots of any/all example pictures', subtask: null, priority: 'Medium'},
            ], priority: 'Medium'},
            {id: 133, name: 'Implement outline', subtask: [
                {id: 1331, name: 'Create any/all tables', subtask: null, priority: 'Low'},
                {id: 1332, name: 'Insert any/all examples', subtask: null, priority: 'Low'},
                {id: 1333, name: 'Format powerpoint', subtask: null, priority: 'Low'},
            ], priority: 'Low'},
            {id: 134, name: 'Test run presentation before submission to Supervisor for approval', subtask: null, priority: 'Low'},
        ], priority: 'Low'},
    ], priority: 'High'},
    {id: 2, name: 'Reorganize desk', subtask: null, priority: 'Low'},
    {id: 3, name: 'Timesheet', subtask: [
        {id: 31, name: 'Compare pre-entered times to actual login/logout times', subtask: [
            {id: 311, name: 'Make adjustments as needed', subtask: null, priority: 'High'},
            {id: 312, name: 'Ensure Holiday times (if any) are included', subtask: null, priority: 'High'},
            {id: 313, name: 'Ensure any sick leave days are included', subtask: null, priority: 'High'},
            {id: 314, name: 'Ensure any days from previous pay period are updated (if needed)', subtask: null, priority: 'High'},
        ], priority: 'High'},
        {id: 32, name: 'Save timesheet after any adjustments', subtask: null, priority: 'High'},
        {id: 33, name: 'Submit timesheet', subtask: null, priority: 'High'},
    ], priority: 'High'},
    {id: 4, name: 'Send Mindful/Positive GIF/message in team chat', subtask: null, priority: 'Low'},
];

console.log(scheduleTasks(taskHierarchy));