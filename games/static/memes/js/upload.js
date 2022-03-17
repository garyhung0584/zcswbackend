async function upload(url) {
  const tag = document.getElementById('tag_name').value;
  const res = await fetch(url, {
    method: 'POST',
    body: {
      name: tag,
    }
  })
  console.log(res);
}