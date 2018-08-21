document.getElementById("edit_comment").addEventListener('click', (evt) => {
	document.getElementById("text_to_change").classList.remove("hidden")
	document.getElementById("submit_change").classList.remove("hidden")
  document.getElementById("submit_change").addEventListener('click', (evt) => {
		document.getElementById("text_to_change").classList.add("hidden")
		document.getElementById("submit_change").classList.add("hidden")
  })
})
