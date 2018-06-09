<template>
    <section>
        <b-field label="Find the latest news in Groningen!">
            <b-autocomplete
                rounded
                v-model="name"
                :data="filteredDataArray"
                placeholder="e.g. Cars"
                icon="magnify"
                @select="option => selected = option">
                <template slot="empty">No results found</template>
            </b-autocomplete>
        </b-field>
      <br></br>
      <section>

        <button class="button is-medium is-success" @click="getNews()">
            Refresh News
        </button>

    </section>
    <br></br>
      <news-collection-list :newsList='newsList'></news-collection-list>
    </section>
</template>

<script>
    import NewsCollectionList from './NewsCollectionList.vue'
    import axios from 'axios';
    export default {
        data() {
            return {
                data: [
                    'No autocomplete terms lol',
                ],
                name: '',
                selected: null,
                newsList: [],
            }
        },
        methods: {
          getNews() {
            let cmp = this;
            axios.get('http://localhost:5000/', {'timeout': 5000})
            .then(function (response) {
                console.log(response.data)
                cmp.newsList = response.data
                cmp.$toast.open({
                    message: 'Newest news fetched successfully!',
                    type: 'is-success',
                    position: 'is-bottom',
                })
              })
              .catch(function (error) {
                console.log(error);
              });
          }
        },
        computed: {
            filteredDataArray() {
                return this.data.filter((option) => {
                    return option
                        .toString()
                        .toLowerCase()
                        .indexOf(this.name.toLowerCase()) >= 0
                })
            }
        },
        components: {
          'news-collection-list': NewsCollectionList
        },
        created(){
          this.getNews()
        }
    }
</script>

<style lang="css">
</style>
