
// function addCourseToApplication(courseId) {
//     $.get('/application/add-course-to-application?course_id=' + courseId).then(res => {
//         console.log(res);
//     });
// }

function addCourseToApplication(courseId) {
    $.get('/application/add-course-to-application?course_id=' + courseId).then(res => {
        console.log(res);
    });
}



