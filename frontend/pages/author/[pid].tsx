import { useRouter } from 'next/router'

const AuthorPid = () => {
    const router = useRouter()
    const { pid } = router.query

    return <p>Author: {pid}</p>
}

export default AuthorPid;
