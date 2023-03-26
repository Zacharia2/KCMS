from tqdm import tqdm
import os
import argparse
import codecs
import json
import re
import requests
requests.session().keep_alive = False  # 及时释放

# https://blog.csdn.net/github_25176023/article/details/105725979

def get_info(comments_url, token):
    headers = {'Content-Type': 'application/json',
               'Authorization': 'token %s' % token}
    r = requests.get(comments_url, headers=headers)
    ret = json.loads(r.text)
    # print(ret)
    if r.status_code > 300:
        print('error %s', r.text)
        return False
    return ret


def to_markdown(page, coms):
    mk = '# ' + page['title'] + '\n'
    mk += "created_at: "+page['created_at']+"\n"
    mk += "updated_at: "+page['updated_at']+"\n"

    labels = "label: "
    for idx, item in enumerate(page['labels']):
        if (idx+1) == len(page['labels']):
            labels += item['name']+'\n'
        else:
            labels += item['name']+','
    mk += labels+'\n'

    mk += page['body']+'\n'

    for com in coms:
        # mk += "\n---\n"
        # mk += "created_at: "+com['created_at'] + \
        #     ", updated_at: "+com['updated_at']+"\n"
        mk += com['body']+"\n"
    return mk


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help="github account username")
    parser.add_argument('-r', '--repo', help="github account repo")
    parser.add_argument('-t', '--token', help="github personal access token")
    parser.add_argument('-o', '--dir', help="out put dir")

    args = parser.parse_args()

    args.username = "Zacharia2"
    args.repo = "Meta-R-Notes"
    args.token = ""
    args.dir = "github_out"

    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    api_url = 'https://api.github.com/repos/%s/%s/issues' % (
        args.username, args.repo)
    issue_ret = get_info(api_url, args.token)
    for page in tqdm(issue_ret):
        coms = []
        if page['comments'] > 0:
            coms = get_info(page['comments_url'], args.token)
        mk = to_markdown(page, coms)

        # save
        filename = page['created_at'].split('T')[0]+','+page['title']+'.md'
        filename = re.sub(r'[/:*?"<>|]', " ", filename)  # check filename
        filename = os.path.join(args.dir, filename)

        with codecs.open(filename, 'w', 'utf-8') as file:
            file.write(mk)

