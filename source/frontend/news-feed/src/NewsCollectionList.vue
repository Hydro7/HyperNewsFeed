<template lang="html">
  <section>
    <div class="container">
      <newsCollection v-for='news in newsList' :newsData="news" ></newsCollection>
    </div>
  </section>
</template>

<script>
import NewsCollection from './NewsCollection.vue';
export default {
  props: ['newsList'],
  components: {
    'newsCollection': NewsCollection
  }
}
</script>

<style lang="css">
</style>
