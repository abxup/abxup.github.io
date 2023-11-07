// 当文档加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 解析查询参数
    const queryParams = new URLSearchParams(window.location.search);
    const postName = queryParams.get('p'); // 从URL中获取p参数

    if (postName) {
        // 构建Markdown文件路径
        const filePath = `post/${postName}.md`;

        // 使用fetch API来加载Markdown文件
        fetch(filePath)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Markdown file not found.');
                }
                return response.text();
            })
            .then(text => {
                // 使用showdown转换Markdown到HTML
                const converter = new showdown.Converter();
                const html = converter.makeHtml(text);
                document.getElementById('content').innerHTML = html;
            })
            .catch(error => {
                document.getElementById('content').innerHTML = '<p>文章加载失败。</p>';
                console.error('Error loading the Markdown file:', error);
            });
    } else {
        document.getElementById('content').innerHTML = '<p>欢迎来到我的博客。</p>';
    }
});
