from markdown_it import MarkdownIt
from markdown_it.rules_inline import StateInline

def replace_foo(state: StateInline, silent: bool):
    content = state.src[state.pos:]
    if content.startswith('foo'):
        state.pos += len('foo')
        state.push('text', '', 0).content = 'bar'
    return True

md = MarkdownIt()
md.inline.ruler.before('text', 'foo_replace', replace_foo)

text = "This is some foo text."
result = md.render(text)
print(result)

replace_foo(state: StateInline, silent: bool):


md.replace("fasdfas", "asdfasdf")