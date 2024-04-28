
// function addCourseToApplication(courseId) {
//     $.get('/application/add-course-to-application?course_id=' + courseId).then(res => {
//         console.log(res);
//     });
// }



function addCourseToApplication(courseId) {
    $.get('/application/add-course-to-application?course_id=' + courseId).then(res => {
              Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        })
    });
}



function removeCourse(courseId) {
    $.get('/application/remove-course?course_id=' + courseId).then(res => {
        console.log(res);
    });
}


function removeVenue(venueId) {
    $.get('/application/remove-venue?venue_id=' + venueId).then(res => {
        console.log(res);
    });
}



function acceptApplication(applicationId) {
    $.get('/application/accept-application?application_id=' + applicationId).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        })
    });
}

function removeActiveApplication(applicationId) {
    $.get('/application/remove-application?application_id=' + applicationId).then(res => {
        console.log(res);
    });
}



function removeAppFromVolunteer(applicationId) {
    $.get('/application/remove-app-from-volunteer?application_id=' + applicationId).then(res => {
        console.log(res);
    });
}

function removeInactiveApplication(applicationId) {
    $.get('/application/remove-inactive-application?application_id=' + applicationId).then(res => {
        console.log(res);
    });
}

function removeVenueInEditMode(applicationId) {
    $.get('/application/remove-venue-of-application?application_id=' + applicationId).then(res => {
        console.log(res);
    });
}