<template>
  <div class="container">
    <h3 class="text-center title">Add new category</h3>
    <form @submit.prevent>
      <div class="mb-3">
        <label for="inputTitle" class="form-label">Title</label>
        <input type="text" class="form-control" id="inputTitle" v-model="category.name">
      </div>
      <div class="mb-3">
        <label for="inputDescription" class="form-label">Description</label>
        <input type="textarea" class="form-control" id="inputDescription" v-model="category.description">
      </div>
      <button class="btn btn-primary" @click="addCategory"><i class="bi bi-file-plus"></i></button>
    </form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        category: {
          name: '',
          description: ''
        },
      }
    },
    methods: {
      addCategory() {
        this.$emit('create', this.category);
        this.category = {
          name: '',
          description: ''
        };
      }
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 20px;
  }
</style>