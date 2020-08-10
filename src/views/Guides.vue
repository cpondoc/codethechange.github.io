<template >
  <div :html="docsHtml">
  </div>
</template>
<script>
import docsHtml from '@/guides/_build/html/index.html'

export default {
  name: 'Guides',
  data () {
    return {
      docsHtml: docsHtml
    }
  }
}
</script>
<style scoped>
.docs_iframe {
    width: 100%;
    border: none;
}
</style>
