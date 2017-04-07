Project features the following modifications from Assignment 2:

- any new forum posts that are submitted are immediately shown under "Recent posts"
- flashed message is shown when a post is submitted
- colour and style changes were added to forum posts for legibility and looks
- changed size and wording of webpage nagivation links
- "top of page" function added to page for convenience

if request.method == 'POST':
        id = request.form['id']
		models.deletePost(id)
        posts = models.retrievePosts()
        return render_template('deletepost.html', posts=posts)


