<template>
    <div class="container">
        <div class="card">
            <div class="card-header text-end">
                Categrory detail
            </div>
            <div class="card-body">
                <h3 class="text-center title">{{ this.$route.params.name }}</h3>
                <!-- <h3 class="card-title">{{ this.$route.params.name }}</h3> -->
                <!-- <h4 class="card-text">{{ this.$route.params.description }}</h4> -->
                <h4 class="text-left my-3 title" >{{ this.$route.params.description }}</h4>
                <router-link class="btn btn-primary me-3" to="/categories">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-skip-backward-fill" viewBox="0 0 16 16">
                        <path d="M.5 3.5A.5.5 0 0 0 0 4v8a.5.5 0 0 0 1 0V8.753l6.267 3.636c.54.313 1.233-.066 1.233-.697v-2.94l6.267 3.636c.54.314 1.233-.065 1.233-.696V4.308c0-.63-.693-1.01-1.233-.696L8.5 7.248v-2.94c0-.63-.692-1.01-1.233-.696L1 7.248V4a.5.5 0 0 0-.5-.5z"/>
                    </svg>
                </router-link>
                <!-- <router-link 
                class="btn btn-warning me-3" 
                :to='{ 
                  name: "categoryEdit", 
                  params: {
                    name: this.$route.params.name, 
                    description: this.$route.params.description, 
                    id: this.$route.params.id 
                    }
                  }'>Edit
                </router-link>
                <router-link class="btn btn-success me-3" :to='{ name: "productAdd", params: {name: this.$route.params.name, id: this.$route.params.id } }'>Add product</router-link>
                <router-link class="btn btn-danger" :to='{ name: "categoryDelete", params: {id: this.$route.params.id }}'>Delete</router-link> -->
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {

}
</script>