<template>
    <div id="refresh">
        Refreshing...
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Refresh',
    methods: {
        refreshConnection() {
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/connect/${userEmail}`
            axios.get(path).then((response) => {
                window.location = response.data.url
            })
        }
    },
    mounted: function() {
        this.refreshConnection();
    }
}
</script>