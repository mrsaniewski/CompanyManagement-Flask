function deleteTask(taskId) {
  fetch("/delete-task", {
    method: "POST",
    body: JSON.stringify({ taskId: taskId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function doneTask(taskId) {
  fetch("/done-task", {
    method: "POST",
    body: JSON.stringify({ taskId: taskId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function donePrize(prizeId) {
  fetch("/done-prize", {
    method: "POST",
    body: JSON.stringify({ prizeId: prizeId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}