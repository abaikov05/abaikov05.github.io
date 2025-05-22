# pages = {
#     "index.html": ["index.html","about-me.html","faq.html","baikal-github-co-blog.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html"],
#     "about-me.html": ["index.html","faq.html","baikal-github-co-blog.html"],
#     "faq.html": ["index.html","about-me.html","baikal-github-co-blog.html"],
#     "baikal-github-co-blog.html": ["index.html","about-me.html","faq.html"],
#     "post2.html": ["index.html","about-me.html","faq.html"],
#     "post3.html": ["index.html","about-me.html","faq.html"],
#     "post4.html": ["index.html","about-me.html","faq.html"],
#     "post5.html": ["index.html","about-me.html","faq.html"],
#     "post6.html": ["index.html","about-me.html","faq.html", "baikal-github-co-blog.html"],
#     "post7.html": ["index.html","about-me.html","faq.html", "baikal-github-co-blog.html"],
#     "post8.html": ["index.html","about-me.html","faq.html", "baikal-github-co-blog.html"],
#     "post9.html": ["index.html","about-me.html","faq.html", "baikal-github-co-blog.html"],
#     "post10.html": ["index.html","about-me.html","faq.html", "baikal-github-co-blog.html"],
#     "golden-dome-of-america.html": ["index.html","about-me.html","faq.html", "baikal-github-co-blog.html"],
# }
pages = {
    "index.html": ["index.html","about-me.html","faq.html","baikal-github-co-blog.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html"],
    "about-me.html": ["index.html","faq.html"],
    "faq.html": ["index.html","about-me.html"],
    "baikal-github-co-blog.html": ["index.html","about-me.html","faq.html","baikal-github-co-blog.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html"],
    "post2.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post3.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post4.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post5.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post6.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post7.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post8.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post9.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "post10.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
    "golden-dome-of-america.html": ["index.html","about-me.html","faq.html","golden-dome-of-america.html","post2.html","post3.html","post4.html","post5.html","post6.html","post7.html","post8.html","post9.html","post10.html", "baikal-github-co-blog.html"],
}
damping = 0.85
num_iterations = 100
num_pages = len(pages)
ranks = {page: 1 / num_pages for page in pages}

for _ in range(num_iterations):
    new_ranks = {}
    for page in pages:
        rank_sum = 0
        for other_page in pages:
            if page in pages[other_page]:
                rank_sum += ranks[other_page] / len(pages[other_page])
        new_ranks[page] = (1 - damping) / num_pages + damping * rank_sum
    ranks = new_ranks

for page, rank in ranks.items():
    print(f"{page}: {rank:.4f}")