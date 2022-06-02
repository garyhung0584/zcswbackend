const button = document.getElementById("new_hashtag_button")
button.addEventListener('click', async (ev) => {
  await upload(tagUrl);
  ev.preventDefault();
})

async function upload(url) {
  const name = document.getElementById('new_hashtag').value;
  const form = new FormData();
  form.append('name', name);
  const res = await fetch(url, {
    method: 'POST',
    body: form,
  })
  if (res.status != 200) {
    throw Error(await res.text())
  }
  const tag = await res.json();

  const elem = document.createElement("label");
  elem.innerHTML = `
    <input type="checkbox" name="tags" value="${tag.id}">
    <span>${tag.name}</span>`
  console.log(elem)
  document.getElementById('hashtag_div').appendChild(elem);
  document.getElementById('new_hashtag').value = ""
  return false
}