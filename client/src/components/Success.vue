<template>
    <div id="success">
        <b-alert variant="success" show>
            Checkout was successful!
        </b-alert>
        <b-button style="margin-right: 15px;" @click="$router.push('/rented-spots')">View Rented Spots</b-button>
    </div>
</template>

<script>
export default {
    name: 'Success',
}
</script>