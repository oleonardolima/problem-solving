num_chapters = int(input())

chapters = []
for line in range(num_chapters):
    chapter = [int(num) for num in input().split(" ")]
    chapters.append(tuple(chapter))

# print(chapters)
marked_page = int(input())

for idx, chapter in enumerate(chapters):
    if marked_page >= chapter[0] and marked_page <= chapter[1]:
        stopped_chapter = idx
        break
    # if marked_page >= chapter[0] and marked_page <= chapter[1]:
    #     stopped_chapter = idx + 1
    #     break


chapters_not_read = num_chapters - stopped_chapter
print(chapters_not_read)