<template>
    <p> we;re in custom form with special property: {{ content }}</p>
</template>
<script>
export default {
  name: 'CustomForm',
  props: [ 'content' ]
}
</script>
