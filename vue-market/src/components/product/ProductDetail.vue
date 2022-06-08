<template>
    <div class="container">
        <div class="card container">
            <div class="card-header">
                <img :src="this.$route.params.image" alt="" class="img-thumbnail ms-auto me-auto">
            </div>
            <div class="card-body">
                
                <table class="table table-striped">
                
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Title</td>
                            <td>{{ this.$route.params.name }}</td>
                        </tr>
                        <tr>
                            <td>Description</td>
                            <td>{{ this.$route.params.description }}</td>
                        </tr>
                        <tr>
                            <td>Price</td>
                            <td>{{ this.$route.params.price }} UZS</td>
                        </tr>
                        <tr>
                            <td>Category</td>
                            <td>{{ this.$route.params.category }}</td>
                        </tr>
                        <tr>
                            <td>image</td>
                            <td><img src="" alt=""></td>
                        </tr>
                        <tr>
                            <td>Quantity</td>
                            <td>{{ this.$route.params.quantity }}</td>
                        </tr>
                        <tr>
                            <td>Unit</td>
                            <td>{{ this.$route.params.unit }}</td>
                        </tr>
                        <tr>
                            <td>Barcode</td>
                            <td>{{ this.$route.params.barcode }}</td>
                        </tr>
                        <tr>
                            <td>Created at</td>
                            <td>{{ this.$route.params.created_at }}</td>
                        </tr>
                        <tr v-if="this.$route.params.is_expired === 'false'">
                            <td>No expire</td>
                            <td>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
                                    <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
                                </svg>
                            </td>
                        </tr>
                        <tr v-else>
                            <td>expiration date</td>
                            <td>{{ this.$route.params.expiration_date }}</td>
                        </tr>
                        <tr>
                            <td>Is visible</td>
                            <td v-if="this.$route.params.is_visible">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
                                    <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
                                </svg>
                            </td>
                            <td v-else>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
                                    <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
                                </svg>
                            </td>

                        </tr>
                    </tbody>
                </table>
                <router-link class="btn btn-primary me-3" to="/products">Back</router-link>
                <router-link class="btn btn-danger" :to='{ name: "productDelete", params: {id: this.$route.params.id } }'>Delete</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  img {
    max-width: 100%;
    max-height: 100%;
  }

</style>