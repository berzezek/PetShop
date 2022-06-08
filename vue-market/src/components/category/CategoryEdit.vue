<template>
  <div class="container">
    <h2 class="text-center title">Edit category</h2>
    <form @submit.prevent>
      <div class="mb-3">
        <label for="inputTitle" class="form-label">Title</label>
        <input type="text" class="form-control" id="inputTitle" v-model="category.name" required>
      </div>
      <div class="mb-3">
        <label for="inputDescription" class="form-label">Description</label>
        <input type="textarea" class="form-control" id="inputDescription" v-model="category.description">
      </div>
      <button class="btn btn-primary me-3" @click="editCategory">Edit</button>
      <router-link class="btn btn-primary" to="/categories">Cancel</router-link>
    </form>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        category: {
          name: this.$route.params.name,
          description: this.$route.params.description,
        },
      }
    },
    props: {
      id: [String, Number]
    },
    methods: {
      async editCategory() {
        await axios.put(`categoryedit/${this.$route.params.id}/`, {
          
          name: this.category.name,
          description: this.category.description
        }).then(response => {
          console.log(response);
          if (response.status == 200) {
            alert('Category edited');
            this.$router.push('/categories');
          } else {
            alert('Category not edited');
          }
        })
      }
    },
  }
</script>

<style scoped>

</style>