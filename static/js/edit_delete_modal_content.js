/**
 * Adds the ability to trigger the delete confirmation modal and 
 * sets its contents depending on whether it was triggered by a 
 * post or comment.
 */
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButtons = document.getElementsByClassName("delete-post-button");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModalLabel = document.getElementById("deleteModalLabel");
const deleteModalBody = document.getElementById("deleteModalBody");

for (let button of deletePostButtons) {
  button.addEventListener("click", (e) => {
    updateModal(e);
    deleteModal.show();
  });
}

/**
 * Updates the delete modal content depending on whether it was triggered
 * from a post or comment.
 *
 * @param {Event} e - The event object from the button click.
 * @param {string} contentType - The type of content being deleted.
 */
function updateModal(e) {
  let contentId = e.target.getAttribute('data-post-id');
  deleteConfirm.href = `/delete-post/${contentId}`;
}