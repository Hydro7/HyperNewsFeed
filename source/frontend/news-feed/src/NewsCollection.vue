<template lang="html">
  <article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img :src="getImage">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>News Title Here</strong> <small>{{getDate}}</small>
        <br>
        {{getNews}}
      </p>
    </div>
    <nav class="level is-mobile">
      <div class="level-left">
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-reply"></i></span>
        </a>
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-retweet"></i></span>
        </a>
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-heart"></i></span>
        </a>
      </div>
    </nav>
  </div>
  <div class="media-right">
  </div>
</article>
</template>

<script>
export default {
  props: ['newsData'],
  computed: {
    getNews() {
      return this.newsData.content;
    },
    getDate() {
      return this.newsData.created_date;
    },
    getImage() {
      if (this.newsData.icon_url == ""){
        return "src/assets/n.png";
      }
      return this.newsData.icon_url;
    }
  }
}
</script>

<style lang="css">
</style>
