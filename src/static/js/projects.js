const projectDescription = (project) => {
    let content = `
        <li class="btn btn-outline-info">
            <a data-bs-toggle="collapse"
               href="#collapseExample${project.id}"
               role="button" aria-expanded="false"
               aria-controls="collapseExample${project.id}">
                Description
            </a>
        </li>
        `
    return content
}


const skillsContent = (skills) => {

    return `
       <div class="col-lg-7 col-md-12">
            <ul class="text-start mt-1" style="padding-left: 0">
                ${skills.map(skill => `<li class="btn btn-outline-primary me-1 mb-1" style="font-size:0.95rem;">${skill.toUpperCase()}</li>`).join('')}
            </ul>
       </div>
       `
}

const projectContent = (project) => {
    return `
            <div class="col-lg-6 col-md-12 portfolio-item my-2">
                <div class="px-3 pt-3 bg-light border border-secondary border-opacity-10 shadow rounded">

                <h4 class="text-center mb-1">${project.title}</h4>
                <video controls autoplay muted loop class="w-100 rounded" width="450" height="350"
                       src="${project.video}">
                    Your browser doesn't support videos!
                </video>
                <div class="row">
                    ${skillsContent(project.skills)}
                    <div class="col-lg-5 col-md-12">
                        <ul class="text-end ms-1">
                            <li class="btn btn-outline-info my-1">
                                <a href="${project.link}" target="_blank">
                                    <i class="bi bi-link"></i> Link
                                </a>
                            </li>
                        ${projectDescription(project)}

                        </ul>
                    </div>
                </div>

                <div class="collapse" id="collapseExample${project.id}">
                    <div class="card card-body overflow-auto mb-3"
                         style="height:6rem">${project.description}</div>
                </div>
            </div>
        </div>


    `
}


function getProjects(skill = null) {
    let url = "/api/portfolio/"
    if (skill !== null) {
        url = url + `?skill=${skill.toLowerCase()}`
    }
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: function (data) {
            let dataContainer = $("#portfolio-container");
            dataContainer.empty();
            data.forEach((element) => {
                htmlContent = `
          ${projectContent(element)}
          `;
                dataContainer.append(htmlContent);
            });
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        },
    });
}

const sendMessage = (data, url, csrfToken) => {
$.ajax({
    url: url,
    type: "POST",
    data: data,
    dataType: "json",
    contentType: false,
    processData: false,
    headers: {
      "X-CSRFToken": csrfToken
    },
    success: function (data) {
      // Clear the form
      $("#name").val("");
      $("#email").val("");
      $("#subject").val("");
      $("#message").val("");
      let alertSuccess = $(".alert-success");
      alertSuccess.removeClass("d-none");
    

    },
    error: function (xhr, status, error) {
      console.log("Error:", error);
      let alertError = $(".alert-danger");
      alertError.removeClass("d-none");
      alertError.text(`An error occurred while sending the message.`);
    },
  });
}

$(document).ready(function () {
    // calling the function to get projects
    getProjects();
    $("#message-form").submit(function (e) {
        e.preventDefault(); // Prevent the default form submission
        var formData = new FormData(this);
        var csrfToken = jQuery("[name=csrfmiddlewaretoken]").val();
        sendMessage(formData, "/api/send-message/", csrfToken)
      });
});